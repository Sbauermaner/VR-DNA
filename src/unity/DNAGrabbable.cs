using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;
using System.Collections;
using UnityEngine.Networking;
using System.Text;

public class DNAGrabbable : XRGrabInteractable
{
    public Transform leftGrab, rightGrab;
    public LineRenderer dnaStrand;
    private float originalLength;

    void Start()
    {
        originalLength = Vector3.Distance(leftGrab.position, rightGrab.position);
    }

    void Update()
    {
        float currentLength = Vector3.Distance(leftGrab.position, rightGrab.position);
        float scaleMultiplier = Mathf.Clamp(currentLength / originalLength, 0.8f, 1.5f);
        dnaStrand.transform.localScale = new Vector3(1, 1, scaleMultiplier);

        if (scaleMultiplier > 1.2f)
        {
            GetComponent<Renderer>().material.color = Color.red;
            StartCoroutine(AnalyzeStretch(scaleMultiplier));
        }
        else
        {
            GetComponent<Renderer>().material.color = Color.white;
        }
    }

    IEnumerator AnalyzeStretch(float stretchFactor)
    {
        string json = $"{{\"stretch_values\": [{stretchFactor}]}}";
        using (UnityWebRequest request = UnityWebRequest.Post("http://localhost:5000/analyze_dna", json))
        {
            byte[] body = Encoding.UTF8.GetBytes(json);
            request.uploadHandler = new UploadHandlerRaw(body);
            yield return request.SendWebRequest();
            Debug.Log("Mutation risk: " + request.downloadHandler.text);
        }
    }
}
