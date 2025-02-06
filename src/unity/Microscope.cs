using UnityEngine;

public class Microscope : MonoBehaviour
{
    public Transform lens;
    public float zoomSpeed = 0.1f;

    void Update()
    {
        if (Input.GetKey(KeyCode.UpArrow)) lens.localScale += Vector3.one * zoomSpeed * Time.deltaTime;
        if (Input.GetKey(KeyCode.DownArrow)) lens.localScale -= Vector3.one * zoomSpeed * Time.deltaTime;
    }
}
