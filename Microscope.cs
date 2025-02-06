using UnityEngine;

public class Microscope : MonoBehaviour
{
    public Camera microscopeCamera;
    public float zoomFactor = 2.0f;
    
    public void AdjustFocus(float adjustment)
    {
        microscopeCamera.fieldOfView = Mathf.Clamp(microscopeCamera.fieldOfView - adjustment, 5, 50);
        Debug.Log("Microscope focus adjusted: " + microscopeCamera.fieldOfView);
    }
}
