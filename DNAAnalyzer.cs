using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class DNAAnalyzer : MonoBehaviour
{
    public void AnalyzeSample(string dnaSequence)
    {
        StartCoroutine(SendToAI(dnaSequence));
    }

    IEnumerator SendToAI(string sequence)
    {
        string json = $"{{\"dna_sequence\": \"{sequence}\"}}";
        using (UnityWebRequest request = UnityWebRequest.Post("http://localhost:5000/analyze_dna", json))
        {
            byte[] body = System.Text.Encoding.UTF8.GetBytes(json);
            request.uploadHandler = new UploadHandlerRaw(body);
            yield return request.SendWebRequest();
            Debug.Log("AI Analysis Result: " + request.downloadHandler.text);
        }
    }
}
