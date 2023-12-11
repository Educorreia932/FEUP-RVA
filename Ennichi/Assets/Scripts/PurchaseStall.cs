using UnityEngine;

public class PurchaseStall : MonoBehaviour {
	public GameObject item;
	public int cost;
	public PlayerController player;
	public Transform spawnPoint;

	public void PurchaseItem() {
		if (player.points < cost)
			return;

		Instantiate(item, spawnPoint);
		player.points -= cost;
	}
}