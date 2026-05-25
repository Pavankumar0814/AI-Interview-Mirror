import cv2
import mediapipe as mp

def detect_cheating():

    camera = cv2.VideoCapture(0)

    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    while True:

        success, frame = camera.read()

        frame = cv2.flip(frame, 1)

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(rgb_frame)

        warning = "Looking Forward"

        if results.multi_face_landmarks:

            for face_landmarks in results.multi_face_landmarks:

                # Nose landmark
                nose = face_landmarks.landmark[1]

                # Check direction
                if nose.x < 0.35:
                    warning = "Looking Left - Suspicious"

                elif nose.x > 0.65:
                    warning = "Looking Right - Suspicious"

                else:
                    warning = "Looking Forward"

        cv2.putText(
            frame,
            warning,
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        cv2.imshow("Cheating Detection", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()