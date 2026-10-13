from PyQt6.QtWidgets import QMainWindow, QFrame, QGridLayout, QVBoxLayout, QLabel, QHBoxLayout
from modules.app import app 
from PyQt6.QtCore import Qt


main_window = QMainWindow()

WIDTH_WINDOW = 800
HEIGHT_WINDOW  = 600

primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)




main_frame = QFrame(parent = main_window)
main_frame.setFixedSize(WIDTH_WINDOW,HEIGHT_WINDOW)
main_frame.setStyleSheet("background-color: black")

main_layout = QGridLayout()
main_frame.setLayout(main_layout)



#  перший ряд

frame_1 = QFrame(parent = main_frame)
frame_1.setFixedSize(220, 180)
frame_1.setStyleSheet("background-color: #F24805; border-radius: 15px ")

main_layout.addWidget(frame_1, 1, 1)

frame1_layout = QVBoxLayout()
frame_1.setLayout(frame1_layout)





frame1_text1 = QLabel(text = "Температура", )
frame1_text1.setStyleSheet("color: white; font-size: 15px ")
frame1_layout.addWidget(frame1_text1)

frame1_layout.addStretch(1)

frame1_text2= QLabel(text = "24°C", )
frame1_text2.setStyleSheet("color: white; font-size: 24px; font-weight: bold")
frame1_layout.addWidget(frame1_text2)

frame1_text3= QLabel(text = "сонячно", )
frame1_text3.setStyleSheet("color: #99FFFFFF; font-size: 13px ")
frame1_layout.addWidget(frame1_text3)


frame_2 = QFrame(parent = main_frame)
frame_2.setFixedSize(220, 180)
frame_2.setStyleSheet("background-color: #0066FF; border-radius: 15px ")

main_layout.addWidget(frame_2, 1, 2)

frame2_layout = QVBoxLayout()
frame_2.setLayout(frame2_layout)

frame2_text1 = QLabel(text = "Вологість", )
frame2_text1.setStyleSheet("color: white; font-size: 15px ")
frame2_layout.addWidget(frame2_text1)

frame2_layout.addStretch(1)

frame2_text2= QLabel(text = "65%", )
frame2_text2.setStyleSheet("color: white; font-size: 24px; font-weight: bold")
frame2_layout.addWidget(frame2_text2)

frame2_text3= QLabel(text = "комфортно", )
frame2_text3.setStyleSheet("color: #99FFFFFF; font-size: 13px ")
frame2_layout.addWidget(frame2_text3)



frame_3 = QFrame(parent = main_frame)
frame_3.setFixedSize(220, 180)
frame_3.setStyleSheet("background-color: #7F30FF ; border-radius: 15px ")

main_layout.addWidget(frame_3, 1, 3)


frame3_layout = QVBoxLayout()
frame_3.setLayout(frame3_layout)

frame3_text1 = QLabel(text = "Швидкість Вітру", )
frame3_text1.setStyleSheet("color: white; font-size: 15px ")
frame3_layout.addWidget(frame3_text1)

frame3_layout.addStretch(1)



frame3_text2= QLabel(text = "12 км/год", )
frame3_text2.setStyleSheet("color: white; font-size: 24px; font-weight: bold")
frame3_layout.addWidget(frame3_text2)

frame3_text3= QLabel(text = "Слабкий вітер", )
frame3_text3.setStyleSheet("color: #99FFFFFF; font-size: 13px ")
frame3_layout.addWidget(frame3_text3)


#  другий ряд 


frame_4 = QFrame(parent = main_frame)
frame_4.setFixedSize(220, 180)
frame_4.setStyleSheet("background-color: #D20163; border-radius: 15px ")

main_layout.addWidget(frame_4, 2, 1)

frame4_layout = QVBoxLayout()
frame_4.setLayout(frame4_layout)


frame4_text1 = QLabel(text = "Відчуваєтся як", )
frame4_text1.setStyleSheet("color: white; font-size: 15px ")
frame4_layout.addWidget(frame4_text1)

frame4_layout.addStretch(1)

frame4_text2= QLabel(text = "27°C", )
frame4_text2.setStyleSheet("color: white; font-size: 24px; font-weight: bold")
frame4_layout.addWidget(frame4_text2)



frame4_text3= QLabel(text = "Тепліше, ніж зазвичай", )
frame4_text3.setStyleSheet("color: #99FFFFFF; font-size: 13px ")
frame4_layout.addWidget(frame4_text3)



frame_5 = QFrame(parent = main_frame)
frame_5.setFixedSize(220, 180)
frame_5.setStyleSheet("background-color: #007799; border-radius: 15px ")

main_layout.addWidget(frame_5, 2, 2)


frame5_layout = QVBoxLayout()
frame_5.setLayout(frame5_layout)



frame5_text1 = QLabel(text = "Атмосферний тиск", )
frame5_text1.setStyleSheet("color: white; font-size: 15px ")
frame5_layout.addWidget(frame5_text1)

frame5_layout.addStretch(1)


frame5_text2= QLabel(text = "760", )
frame5_text2.setStyleSheet("color: white; font-size: 24px; font-weight: bold")
frame5_layout.addWidget(frame5_text2)



frame5_text3= QLabel(text = "мм рт. ст.", )
frame5_text3.setStyleSheet("color: #99FFFFFF; font-size: 13px ")
frame5_layout.addWidget(frame5_text3)




frame_6 = QFrame(parent = main_frame)
frame_6.setFixedSize(220, 180)
frame_6.setStyleSheet("background-color: #00875A ; border-radius: 15px ")

main_layout.addWidget(frame_6, 2, 3)


frame6_layout = QVBoxLayout()
frame_6.setLayout(frame6_layout)


frame6_text1 = QLabel(text = "Ймовірність дощу", )
frame6_text1.setStyleSheet("color: white; font-size: 15px ")
frame6_layout.addWidget(frame6_text1)

frame6_layout.addStretch(1)

frame6_text2= QLabel(text = "20%", )
frame6_text2.setStyleSheet("color: white; font-size: 24px; font-weight: bold")
frame6_layout.addWidget(frame6_text2)


frame6_text3= QLabel(text = "Невелика", )
frame6_text3.setStyleSheet("color: #99FFFFFF; font-size: 13px ")
frame6_layout.addWidget(frame6_text3)


# 3 рядок


frame_7 = QFrame(parent = main_frame)
frame_7.setFixedSize(220, 180)
frame_7.setStyleSheet("background-color: #282C3C; border-radius: 15px ")

main_layout.addWidget(frame_7, 3, 1)

frame7_layout = QVBoxLayout()
frame_7.setLayout(frame7_layout)

frame7_layout.addStretch(1)

frame7_text1 = QLabel(text = "Керування погодою")
frame7_layout.addWidget(frame7_text1)
frame7_text1.setAlignment(Qt.AlignmentFlag.AlignCenter)

frame7_layout.addStretch(1)


frame_7_1 = QFrame(parent = frame_7)

frame_7_1.setFixedSize(200, 35)
frame_7_1.setStyleSheet("background-color: #5152FF; border-radius: 10px ")
frame7_layout.addWidget(frame_7_1)


frame_7_1layout = QVBoxLayout()
frame_7_1.setLayout(frame_7_1layout)


frame_7_1_text = QLabel(text = "оновити")
frame_7_1_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

frame_7_1layout.addWidget(frame_7_1_text)



frame_8 = QFrame(parent = main_frame)
frame_8.setFixedSize(220, 180)
frame_8.setStyleSheet("background-color: #2A3A4E; border-radius: 15px ")

main_layout.addWidget(frame_8, 3, 2)

frame8_layout = QVBoxLayout()
frame_8.setLayout(frame8_layout)


frame8_text1 = QLabel(text = "Місто", )
frame8_text1.setStyleSheet("color: white; font-size: 15px ")
frame8_layout.addWidget(frame8_text1)

frame8_layout.addStretch(1)


frame8_text2= QLabel(text = "Дніпро", )
frame8_text2.setStyleSheet("color: white; font-size: 24px; font-weight: bold")
frame8_layout.addWidget(frame8_text2)


frame8_text3= QLabel(text = "Україна", )
frame8_text3.setStyleSheet("color: white; font-size: 13px ")
frame8_layout.addWidget(frame8_text3)






frame_9 = QFrame(parent = main_frame)
frame_9.setFixedSize(220, 180)
frame_9.setStyleSheet("background-color: #242836; border-radius: 15px ")

main_layout.addWidget(frame_9, 3, 3)

frame9_layout = QVBoxLayout()
frame_9.setLayout(frame9_layout)

frame9_layout.addStretch(1)


frame9_text1 = QLabel(text = "стан погоди")
frame9_layout.addWidget(frame9_text1)
frame9_text1.setAlignment(Qt.AlignmentFlag.AlignCenter)



frame9_layout.addStretch(1)


frame_9_1 = QFrame(parent = frame_9)

frame_9_1.setFixedSize(200, 35)
frame_9_1.setStyleSheet("background-color: #00BA7A; border-radius: 10px ")
frame9_layout.addWidget(frame_9_1)



rame_9_1layout = QVBoxLayout()
frame_9_1.setLayout(rame_9_1layout)


frame_9_1_text = QLabel(text = "Змінити колір")
frame_9_1_text.setAlignment(Qt.AlignmentFlag.AlignCenter)

rame_9_1layout.addWidget(frame_9_1_text)
