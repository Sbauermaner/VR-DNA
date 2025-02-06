using UnityEngine;
using UnityEngine.XR.Interaction.Toolkit;

public class LabObject : XRGrabInteractable
{
    public bool isLiquid;
    public Color liquidColor;
    public float volume;

    protected override void OnSelectEntered(SelectEnterEventArgs args)
    {
        base.OnSelectEntered(args);
        if (isLiquid) PourLiquid();
    }

    void PourLiquid()
    {
        Debug.Log("Liquid poured: " + volume + "ml of " + liquidColor.ToString());
    }
}
