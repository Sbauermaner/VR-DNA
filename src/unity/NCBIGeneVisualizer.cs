using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class NCBIGeneVisualizer : MonoBehaviour {
    public IEnumerator FetchGeneData(string geneId) {
        using (UnityWebRequest request = UnityWebRequest.Get($"http://localhost:5000/gene/{geneId}")) {
            yield return request.SendWebRequest();
            if (request.result == UnityWebRequest.Result.Success) {
                Debug.Log($"Данные гена: {request.downloadHandler.text}");
            } else {
                Debug.LogError($"Ошибка: {request.error}");
            }
        }
    }
}
