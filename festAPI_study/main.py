import sqlite3
import pandas as pd
import xlsxwriter
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 할 일 데이터 모델 정의
class TodoItem(BaseModel):
    task: str
    completed: bool

# SQLite3 데이터베이스 초기화
conn = sqlite3.connect('todo.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS todo
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              task TEXT NOT NULL,
              completed BOOLEAN NOT NULL DEFAULT 0);''')
conn.commit()
conn.close()

# FastAPI 애플리케이션 실행 시 실행되는 함수
@app.on_event("startup")
def startup_event():
    global df
    conn = sqlite3.connect('todo.db')
    df = pd.read_sql_query("SELECT * from todo", conn)
    # 데이터베이스에서 모든 할 일 목록을 pandas 데이터프레임으로 가져와 전역 변수 df에 저장합니다.
    conn.close()

# 할 일 목록 추가 엔드포인트
@app.post("/todo")
def add_todo_item(item: TodoItem):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO todo (task, completed) VALUES (?, ?)", (item.task, item.completed))
    conn.commit()
    conn.close()
    create_excel_file()
    # 할 일 목록에 변경이 생길 때마다 엑셀 파일을 생성하는 create_excel_file 함수를 호출합니다.
    return {"message": "Todo item added."}

# 할 일 목록 수정 엔드포인트
@app.put("/todo/{item_id}")
def update_todo_item(item_id: int, item: TodoItem):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("UPDATE todo SET task = ?, completed = ? WHERE id = ?", (item.task, item.completed, item_id))
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.commit()
    conn.close()
    create_excel_file()
    # 할 일 목록에 변경이 생길 때마다 엑셀 파일을 생성하는 create_excel_file 함수를 호출합니다.
    return {"message": "Todo item updated."}

# 할 일 목록 삭제 엔드포인트
@app.delete("/todo/{item_id}")
def delete_todo_item(item_id: int):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE FROM todo WHERE id = ?", (item_id,))
    if c.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.commit()
    conn.close()
    create_excel_file()
    # 할 일 목록에 변경이 생길 때마다 엑셀 파일을 생성하는 create_excel_file 함수를 호출합니다.
    return {"message": "Todo item deleted."}

# 엑셀 파일 생성 함수
def create_excel_file():
    conn = sqlite3.connect('todo.db')
    df = pd.read_sql_query("SELECT * from todo", conn)
    conn.close()

    # 엑셀 파일 생성
    writer = pd.ExcelWriter('my_result.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    # pandas로 SQLite 데이터베이스에서 가져온 데이터를 엑셀 파일로 저장합니다.

# 테스트용 코드
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
