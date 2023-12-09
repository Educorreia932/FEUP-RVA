using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Target : MonoBehaviour
{
    public Transform targetTransform;
    public Transform targetCenter;
    public Transform targetEdge;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnCollisionEnter(Collision collision) {
		if (collision.collider.tag == "Dart") {
			Destroy(collision.collider.GetComponent<Rigidbody>());
            collision.collider.transform.eulerAngles = targetTransform.eulerAngles;
            float radius = Vector3.Distance(targetCenter.position, targetEdge.position);
            float hitRadius = Vector3.Distance(targetCenter.position, collision.collider.transform.position);
            float ratio = hitRadius / radius;
            if (ratio >= 1.0f) {
                Debug.Log("Outside");
            } else {
                int score =  (int) -(10.0f * (ratio - 1.0f));
                Debug.Log(score);
            }
		}
	}
}
