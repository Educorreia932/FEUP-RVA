using UnityEngine;

public class GetDestroyed : MonoBehaviour {
	public GameManager gameManager;

	private void OnCollisionEnter(Collision collision) {
		switch (collision.collider.tag) {
			case "Ball":
				Debug.Log("Collided with ball");
				gameManager.BallFell();
				Destroy(collision.collider.gameObject);

				break;

			case "Can":
				gameManager.CanFell();
				Destroy(collision.collider.gameObject);

				break;
		}
	}
}