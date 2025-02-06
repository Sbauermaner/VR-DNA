using UnityEngine;

public class LabExperiment : MonoBehaviour
{
    public GameObject reagent;
    private bool reactionStarted = false;

    void OnTriggerEnter(Collider other)
    {
        if (other.gameObject == reagent && !reactionStarted)
        {
            Debug.Log("Reaction started!");
            reactionStarted = true;
        }
    }
}
