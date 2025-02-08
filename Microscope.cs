using UnityEngine;

public class Microscope : MonoBehaviour {
    public Camera microscopeCamera;

    public void ZoomIn() {
        microscopeCamera.fieldOfView = Mathf.Max(10, microscopeCamera.fieldOfView - 5);
    }

    public void ZoomOut() {
        microscopeCamera.fieldOfView = Mathf.Min(60, microscopeCamera.fieldOfView + 5);
    }
}
