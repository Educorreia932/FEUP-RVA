using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BallGameController : MonoBehaviour {
	public GameObject ballPrefab;
	public Transform firePoint;

	// Start is called before the first frame update
	void Start() {
	}

	// Update is called once per frame
	void Update() {
		if (Input.GetKeyDown(KeyCode.Space))
			ThrowBall();
	}

	void ThrowBall() {
		float speed = 10.0f;
		GameObject ball = Instantiate(ballPrefab, firePoint.position, firePoint.rotation);
		Rigidbody ballRb = ball.GetComponent<Rigidbody>();
		ballRb.AddForce(-transform.right * speed, ForceMode.Impulse);
	}
}