import cv2

# Part 1 – Image Processing Module
image = cv2.imread("student_id.jpg")

if image is None:
    print("Error: student_id.jpg not found!")
else:
    print("Image Loaded Successfully!")

    cv2.imshow("Original Image", image)

    cv2.imwrite("backup.jpg", image)

    resized = cv2.resize(image, (300, 300))
    print("Image Resized to 300x300")
    cv2.imshow("Resized Image", resized)

    cropped = resized[50:200, 100:250]
    print("Cropped Region Displayed")
    cv2.imshow("Cropped Image", cropped)

    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    print("Converted to Grayscale")
    cv2.imshow("Grayscale Image", gray)

    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    print("Converted to HSV")
    cv2.imshow("HSV Image", hsv)

    blur = cv2.GaussianBlur(resized, (15, 15), 0)
    print("Blur Applied")
    cv2.imshow("Blurred Image", blur)

    print("Image Processing Module Completed!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Part 2 – Video Processing Module
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot open camera")
else:
    print("Camera Started...")
    print("Press 'q' to Exit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Smart Campus Camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Camera Closed Successfully")
