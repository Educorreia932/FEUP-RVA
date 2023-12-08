using UnityEngine;

public class GetDestroyed : MonoBehaviour {
	private void OnCollisionEnter(Collision collision) {
		if (collision.collider.name == "Destroyer") {
			Destroy(gameObject);
		}
	}
}