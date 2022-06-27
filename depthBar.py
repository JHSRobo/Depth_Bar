import cv2
import numpy as np

def main():
    counter = 10
    while True:
        # Preparing the bar
        img = np.zeros([1024,1536,3],dtype=np.uint8)
        img = cv2.line(img, (900, 94), (900, 900), (0, 0, 255), 10)
        img = cv2.line(img, (900, 94), (850, 94), (0, 0, 255), 10)
        img = cv2.putText(img, '0 ft', (935, 104), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        img = cv2.line(img, (900, 900), (850, 900), (0, 0, 255), 10)

        # Sample depth hold target
        depthHold = -7.4
        target = abs(94 - (depthHold * 61.55))
        
        img = cv2.line(img, (800, int(target)), (1050, int(target)), (255, 0, 0), 10)
        img = cv2.putText(img, 'Target: {:.2f} ft'.format(depthHold), (1070, int(target) + 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        # Intervals (31 pixels)
        for i in range(25):
            # Every half foot
            if i % 2 == 0:
                img = cv2.line(img, (900, 869 - (i * 31)), (875, 869 - (i * 31)), (0, 0, 255), 10)
            # Every whole foot
            else:
                img = cv2.line(img, (900, 869 - (i * 31)), (850, 869 - (i * 31)), (0, 0, 255), 10)
            # Annotate every interval of 2 ft
            if (i / 2) % 2 == 0 and i != 24:
                img = cv2.putText(img, '-{} ft'.format(12 - (i / 2)), (935, 848 - (i * 31)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        # Draw pointer
        point1 = (900, (counter * 10))
        point2 = (850, (counter * 10) + 25)
        point3 = (850, (counter * 10) - 25)

        pointer = np.array([point1, point2, point3])
        cv2.drawContours(img, [pointer], 0, (0,255,0), -1)

        img = cv2.putText(img, '{:.2f} ft'.format(-(((counter - 10) * 10) / 61.55)), (675, (counter * 10) + 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Keys to raise and lower the bar
        k = cv2.waitKey(1)
        if k == ord('w'):
            if counter > 10:
                counter = counter - 1
        if k == ord('s'):
            if counter < 90:
                counter = counter + 1
        
        # Display
        cv2.imshow("image", img)
        if k == ord('q'):
            cv2.destroyAllWindows()
            break

main()
