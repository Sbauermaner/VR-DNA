using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

public class DNAGrabbable : XRGrabInteractable
{
    protected override void OnSelectEntered(SelectEnterEventArgs args)
    {
        base.OnSelectEntered(args);
        Debug.Log("DNA strand selected.");
    }
}
