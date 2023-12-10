using UnityEngine;

public class DartsGameManager : GameManager {
	public Transform dartSpawnPoint;
	public GameObject dartPrefab;

	private int numDarts;
	private int score;
	
	public override void StartGame() {
		Instantiate(dartPrefab, dartSpawnPoint);

		numDarts = 5;
		score = 0;
	}

	protected override void EndGame() {
		canvas.SetActive(true);

		AwardPlayer(score);
	}
		
	public void DartHit(int points) {
		score += points;
		numDarts--;
	}
	
	public void SpawnDart() {
		Instantiate(dartPrefab, dartSpawnPoint);
	}
}