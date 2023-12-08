using System;
using UnityEngine;

public class BallGameController : Game {
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
		ballRb.AddForce(-transform.right + new Vector3(0, 0.3f, 0) * speed, ForceMode.Impulse);
	}
}