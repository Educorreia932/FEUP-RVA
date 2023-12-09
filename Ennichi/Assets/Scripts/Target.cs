using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Target : MonoBehaviour
{
    public Transform targetTransform;
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
		}
	}
}
