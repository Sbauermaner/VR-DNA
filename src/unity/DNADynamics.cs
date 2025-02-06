using UnityEngine;

public class DNADynamics : MonoBehaviour
{
    public float elasticity = 5f;
    public float damping = 0.5f;
    private Rigidbody rb;

    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }

    void FixedUpdate()
    {
        Vector3 force = -elasticity * transform.position - damping * rb.velocity;
        rb.AddForce(force);
    }
}
