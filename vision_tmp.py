import cv2  # OpenCV를 사용하기위해 import해줍니다.
import numpy as np  # 파이썬의 기본 모듈중 하나인 numpy


def main():
    camera = cv2.VideoCapture(0)  # 카메라를 비디오 입력으로 사용. -1은 기본설정이라는 뜻
    camera.set(3, 300)  # 띄울 동영상의 가로사이즈 160픽셀
    camera.set(4, 300)  # 띄울 동영상의 세로사이즈 120픽셀

    while (camera.isOpened()):  # 카메라가 Open되어 있다면,
        ret, frame = camera.read()  # 비디오의 한 프레임씩 읽습니다. ret값이 True, 실패하면 False, fram에 읽은 프레임이 나옴
        frame = cv2.flip(frame, 1)  # 카메라 이미지를 flip, 뒤집습니다. -1은 180도 뒤집는다
        cv2.imshow('Origin', frame)  # 'normal'이라는 이름으로 영상을 출력

        # blue color 검출
        # hsv이미지로 변환
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # blue 영역만 추출하기 위한 임계값 조절
        blue_mask = cv2.inRange(hsv_img, (100, 130, 130), (120, 255, 255))

        # 추출한 blue 이미지 테스트
        #cv2.imshow('blue mask', blue_mask)

        # 영상 노이즈 제거를 위해 morphology 연산
        morph_size = 2

        # 구조화 커널 생성
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (morph_size*2 + 1, morph_size*2 + 1))

        # 닫힘 연산 -> 열림 연산 순서대로 진행하며 노이즈 최대한 제거
        close_img = cv2.morphologyEx(blue_mask, cv2.MORPH_CLOSE, kernel)
        open_img = cv2.morphologyEx(close_img, cv2.MORPH_OPEN, kernel)

        morph_blue = open_img

        #cv2.imshow('morph mask', morph_blue)

        # 원영상과 합치기
        result = cv2.bitwise_and(frame, frame, mask=morph_blue)

        cv2.imshow('result', result)

        mask = cv2.erode(morph_blue, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        cv2.imshow('mask', mask)

        ret, thresh1 = cv2.threshold(mask.copy(), 127, 255, cv2.THRESH_BINARY)

        # 이미지의 윤곽선을 검출
        contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        # 윤곽선이 있다면, max(가장큰값)을 반환, 모멘트를 계산한다.
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            M = cv2.moments(c)

            # X축과 Y축의 무게중심을 구한다.
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])

            # X축의 무게중심을 출력한다.
            teduri = cv2.drawContours(result, contours, -1, (0, 255, 0), 3)
            # cv2.line(teduri, (cx, 0), (cx, 720), (255, 0, 0), 1)
            # cv2.line(teduri, (0, cy), (1280, cy), (255, 0, 0), 1)
            cv2.circle(teduri, (cx, cy), 2, (255, 0, 0), 2)

            cv2.imshow('teduri', teduri)
            print(cx)  # 출력값을 print 한다.

        if cv2.waitKey(1) == ord('q'):  # 만약 q라는 키보드값을 읽으면 종료합니다.
            break

    cv2.destroyAllWindows()  # 이후 openCV창을 종료합니다.

if __name__ == '__main__':
    main()