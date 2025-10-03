import cv2

# Load the Haar Cascade
face_cascade = cv2.CascadeClassifier(r"C:\Users\jhakr\Downloads\project\haarcascade_frontalface_default.xml")

# Start the webcam feed
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Run for a fixed number of frames (or seconds)
frame_count = 0
max_frames = 200  # Stop after 200 frames (~6 seconds at 30 FPS)

while frame_count < max_frames:
    # Read a frame
    success, img = cap.read()
    if not success:
        print("Error: Could not read frame.")
        break

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the image
    cv2.imshow("Live Feed - Press 'q' to Quit", img)
    frame_count += 1

    # Quit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
print("Program ended.")
