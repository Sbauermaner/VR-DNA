using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class NCBIGeneVisualizer : MonoBehaviour
{
    public string geneId = "7157"; // TP53 (tumor suppressor gene)
    private string apiUrl = "https://api.ncbi.nlm.nih.gov/datasets/v1/gene/";

    void Start()
    {
        StartCoroutine(FetchGeneInfo());
    }

    IEnumerator FetchGeneInfo()
    {
        using (UnityWebRequest request = UnityWebRequest.Get(apiUrl + geneId))
        {
            yield return request.SendWebRequest();
            if (request.result == UnityWebRequest.Result.Success)
            {
                Debug.Log("Gene Info: " + request.downloadHandler.text);
            }
            else
            {
                Debug.LogError("Error fetching gene data: " + request.error);
            }
        }
    }
}
