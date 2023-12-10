using UnityEngine;

public abstract class GameManager : MonoBehaviour {
	public GameObject canvas;
	public PlayerController player;
	
	public abstract void StartGame();
	
	protected abstract void EndGame();

	protected void AwardPlayer(int points) {
		player.points += points;
	}
}