using UnityEngine;

public class LiquidReactor : MonoBehaviour
{
    public Color resultColor;

    public void MixLiquids(Color liquid1, Color liquid2)
    {
        resultColor = Color.Lerp(liquid1, liquid2, 0.5f);
        Debug.Log("New liquid color: " + resultColor.ToString());
    }
}
