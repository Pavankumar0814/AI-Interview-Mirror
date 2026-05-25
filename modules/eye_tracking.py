def track_eyes():
    import cv2
    import mediapipe as mp

    # Start webcam
    camera = cv2.VideoCapture(0)

    # Load MediaPipe Face Mesh
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    # Drawing utility
    mp_draw = mp.solutions.drawing_utils

    while True:
        success, frame = camera.read()

        # Flip image
        frame = cv2.flip(frame, 1)

        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process face
        results = face_mesh.process(rgb_frame)

        # If face detected
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:

                # Draw landmarks
                mp_draw.draw_landmarks(
                    frame,
                    face_landmarks,
                    mp_face_mesh.FACEMESH_CONTOURS
                )

                # Display text
                cv2.putText(
                    frame,
                    "Eye Tracking Active",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

        # Show window
        cv2.imshow("Eye Tracking", frame)

        # Press q to quit
        key = cv2.waitKey(10)

        if key == ord('q'):
          break

    camera.release()
    cv2.destroyAllWindows()