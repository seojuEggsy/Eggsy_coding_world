import pygame
import random

# 상수 정의
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
BLOCK_SIZE = 20
COLORS = [(255, 0, 0),    # red
          (0, 255, 0),    # green
          (0, 0, 255),    # blue
          (255, 255, 0),  # yellow
          (255, 0, 255),  # magenta
          (0, 255, 255),  # cyan
          (255, 128, 0),  # orange
          (128, 128, 128),# gray
          (255, 255, 255),# white
          (128, 0, 0),    # dark red
          (0, 128, 0),    # dark green
          (0, 0, 128)]    # dark blue

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class TetrisGame:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Tetris Game")

        self.clock = pygame.time.Clock()

        self.board = [[0 for y in range(BOARD_HEIGHT)] for x in range(BOARD_WIDTH)]
        self.block = [[random.randint(0, 6), random.randint(0, len(COLORS) - 1)],
                      [random.randint(0, 6), random.randint(0, len(COLORS) - 1)],
                      [random.randint(0, 6), random.randint(0, len(COLORS) - 1)],
                      [random.randint(0, 6), random.randint(0, len(COLORS) - 1)]]

        self.score = 0
        self.fall_time = 0
        self.fall_speed = 1000

    def rotate_block(self, block):
        # 블록의 중심점 계산
        center_x = sum([b[0] for b in block]) // 4
        center_y = sum([b[1] for b in block]) // 4

        # 블록을 중심점을 기준으로 이동
        new_block = [[b[0] - center_x, b[1] - center_y] for b in block]

        # 블록 회전
        for i in range(4):
            new_block[i][0], new_block[i][1] = new_block[i][1], -new_block[i][0]

        # 블록을 원래 위치로 이동
        new_block = [[b[0] + center_x, b[1] + center_y] for b in new_block]

        return new_block


    def check_full_rows(self, board):
        full_rows = []
        for y in range(BOARD_HEIGHT):
            if all(board[x][y] != 0 for x in range(BOARD_WIDTH)):
                full_rows.append(y)
        return full_rows

    def remove_rows(self, board, full_rows):
        for y in full_rows:
            for x in range(BOARD_WIDTH):
                for yy in range(y, 0, -1):
                    board[x][yy] = board[x][yy - 1]
                board[x][0] = 0

    def show_game_over_message(self):
        font = pygame.font.SysFont(None, 48)
        text = font.render("GAME OVER", True, WHITE)
        self.screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))

    def reset_game(self):
        for x in range(BOARD_WIDTH):
            for y in range(BOARD_HEIGHT):
                self.board[x][y] = 0

    def game_over(self):
        for b in self.block:
            if b[1] < 0:
                return True
            if self.board[b[0]][b[1]] != 0:
                return True
        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # 게임 오버 처리
            if self.game_over():
                self.show_game_over_message()
                pygame.display.update()
                pygame

            # 시간 업데이트
            self.fall_time += self.clock.get_rawtime()
            self.clock.tick()

            # 블록 이동
            if self.fall_time >= self.fall_speed:
                self.fall_time = 0
                for b in self.block:
                    b[1] += 1

                # 블록이 바닥에 닿으면 게임 보드에 고정
                for b in self.block:
                    if b[1] >= BOARD_HEIGHT:
                        for bb in self.block:
                            if bb[1] >= 0:
                                self.board[bb[0]][bb[1]] = bb[1]
                        self.block = [[random.randint(0, 6), random.randint(0, len(COLORS) - 1)],
                                      [random.randint(0, 6), random.randint(0, len(COLORS) - 1)],
                                      [random.randint(0, 6), random.randint(0, len(COLORS) - 1)],
                                      [random.randint(0, 6), random.randint(0, len(COLORS) - 1)]]

                # 꽉 찬 행 지우기
                full_rows = self.check_full_rows(self.board)
                if full_rows:
                    self.remove_rows(self.board, full_rows)

            # 블록 회전
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.block = self.rotate_block(self.block)

            # 블록 이동
            if keys[pygame.K_LEFT]:
                for b in self.block:
                    b[0] -= 1
                    if b[0] < 0 or self.board[b[0]][b[1]] != 0:
                        for bb in self.block:
                            bb[0] += 1
                        break
            if keys[pygame.K_RIGHT]:
                for b in self.block:
                    b[0] += 1
                    if b[0] >= BOARD_WIDTH or self.board[b[0]][b[1]] != 0:
                        for bb in self.block:
                            bb[0] -= 1
                        break

            # 화면 업데이트
            self.screen.fill(BLACK)

            # 블록 그리기
            for b in self.block:
                pygame.draw.rect(self.screen, COLORS[min(b[1],11)],
                                 (b[0] * BLOCK_SIZE, b[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

            # 고정된 블록 그리기
            for x in range(BOARD_WIDTH):
                for y in range(BOARD_HEIGHT):
                    if self.board[x][y] != 0:
                        pygame.draw.rect(self.screen, WHITE,
                                         (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

            # 게임 정보 그리기
            font = pygame.font.SysFont(None, 24)
            score_text = font.render("Score: " + str(self.score), True, WHITE)
            self.screen.blit(score_text, (10, 10))

            # 화면 업데이트
            pygame.display.update()

if __name__ == '__main__':
    TetrisGame().run()
