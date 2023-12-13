using UnityEngine;

public class GetDestroyed : MonoBehaviour {
	public CansGameManager gameManager;

	private void OnCollisionEnter(Collision collision) {
		switch (collision.collider.tag) {
			case "Ball":
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