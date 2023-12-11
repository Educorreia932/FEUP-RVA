using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Target : MonoBehaviour {
	public Transform targetCenter;
	public Transform targetEdge;

	public DartsGameManager gameManager;

	private void OnCollisionEnter(Collision collision) {
		int score = 0;

		if (collision.collider.CompareTag("Dart")) {
			// Freeze dart
			collision.collider.GetComponent<Rigidbody>().constraints = RigidbodyConstraints.FreezeAll;
			
			// Lock rotation to be perpendicular to target
			collision.collider.transform.eulerAngles = transform.eulerAngles;

			float radius = Vector3.Distance(targetCenter.position, targetEdge.position);
			float hitRadius = Vector3.Distance(targetCenter.position, collision.collider.transform.position);
			float ratio = hitRadius / radius;

			if (ratio < 1.0f)
				score = (int) -(100.0f * (ratio - 1.0f));

			gameManager.DartHit(score);
		}
	}
}