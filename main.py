import dbConn
import cv2
import streamlit as st
from PIL import Image

def capture():
    cap = cv2.VideoCapture('http://192.168.0.46:4747/video')

    while True:
        retval, frame = cap.read()
        if not retval:
            break
        cv2.imshow('frame', frame)
        key = cv2.waitKey(25)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':

    try:
        uploaded_file = st.file_uploader('File uploader')
        img = Image.open(uploaded_file)
        img.save('./temp.jpg')
        st.image(img, caption='Uploaded Image', use_column_width=True)
    except Exception as e:
        st.text(e)

    sql = 'SELECT id, 기상청관측지점번호 FROM weather'   
    data = dbConn.dfFromDB(sql)

    # capture()

    st.table(data)


