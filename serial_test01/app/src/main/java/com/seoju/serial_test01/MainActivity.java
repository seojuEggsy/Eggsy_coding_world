package com.seoju.serial_test01;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.security.InvalidParameterException;

import android_serialport_api.SerialPort;

public class MainActivity extends AppCompatActivity {

    private static final String LOG_TAG = "MainActivity";

    protected SerialPort mSerialPort;
    protected OutputStream mOutputStream;
    private InputStream mInputStream;
    private ReadThread mReadThread;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        try {
            mSerialPort = getSerialPort("/dev/ttyS1",56000);
            mOutputStream = mSerialPort.getOutputStream();
            mInputStream = mSerialPort.getInputStream();

            /* Create a receiving thread */
            mReadThread = new ReadThread();
            mReadThread.start();

            SendReadCardCommand();
        }
        catch (SecurityException e) {
            Log.e(LOG_TAG,e.getMessage());
        }
        catch (InvalidParameterException e) {
            Log.e(LOG_TAG,e.getMessage());
        }
    }

    @Override
    protected void onDestroy() {
        if(mReadThread != null){
            mReadThread.interrupt();
            closeSeiralPort();
            mSerialPort = null;
        }
        super.onDestroy();
    }

    byte bRcvBuf[] = new byte[1024];
    int nOffset = 0;

    protected void onDataReceived(final byte[] buffer, final int size) {
        try {
            System.arraycopy(buffer, 0, bRcvBuf, nOffset, size);
            nOffset += size;
            Log.d(LOG_TAG, "Offset: " + nOffset);
            Log.d(LOG_TAG, "ReadResponse: " + byteArrayToString(bRcvBuf, nOffset));

            bRcvBuf = null;
            bRcvBuf = new byte[1024];
            nOffset = 0;

        } catch (Exception ex) {
            Log.e(LOG_TAG, ex.getMessage());
        }
    }

    private String byteArrayToString(byte[] a,int nSize) {
        StringBuilder sb = new StringBuilder();
        int nBreak = 0;
        for(final byte b: a) {
            sb.append(String.format("0x%02x ", b & 0xff));
            nBreak++;
            if(nBreak >= nSize){
                break;
            }
        }
        return sb.toString();
    }

    public void SendReadCardCommand(){
        byte bSendVal[] = new byte[12];
        bSendVal[0] = (byte)0x02;
        bSendVal[1] = (byte)0x01;
        bSendVal[2] = (byte)0xB0;
        bSendVal[3] = (byte)0x01;
        bSendVal[4] = (byte)0x0E;
        bSendVal[5] = (byte)0x01;
        bSendVal[6] = (byte)0xEA;
        bSendVal[7] = (byte)0x00;
        bSendVal[8] = (byte)0x00;
        bSendVal[9] = (byte)0x48;
        bSendVal[10] = (byte)0xDD;
        bSendVal[11] = (byte)0x03;

        try{
            mOutputStream.write(bSendVal);
        } catch (IOException ex){
            Log.e(LOG_TAG, ex.getMessage());
        }
    }

    private class ReadThread extends Thread {
        @Override
        public void run() {
            super.run();
            while (!isInterrupted()) {
                int size;
                try {
                    byte[] buffer = new byte[64];
                    if (mInputStream == null) return;
                    size = mInputStream.read(buffer);
                    if (size > 0) {
                        onDataReceived(buffer, size);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                    return;
                }
            }
        }
    }

    private SerialPort m_SerialRFID = null;
    private SerialPort m_SerialCARD = null;
    private SerialPort m_Serial = null;

    public SerialPort getSerialPort(String strPortNum , int nBaudrate){
        try {
            if (m_Serial == null) {
                m_Serial = new SerialPort(new File(strPortNum), nBaudrate, 0);
            }
        }
        catch (Exception ex){
            Log.e(LOG_TAG, ex.getMessage());
        }
        return m_Serial;
    }

    public void closeSeiralPort(){
        if(m_Serial != null){
            m_Serial.close();
            m_Serial = null;
        }
    }
}
