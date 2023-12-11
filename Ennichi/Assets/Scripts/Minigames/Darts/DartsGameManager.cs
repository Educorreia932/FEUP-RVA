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
		
		canvas.SetActive(false);
	}

	protected override void EndGame() {
		AwardPlayer(score);
		
		canvas.SetActive(true);
	}
	
	public void SpawnDart() {
		Instantiate(dartPrefab, dartSpawnPoint);
	}
		
	public void DartHit(int points) {
		score += points;
		numDarts--;
		
		if (numDarts == 0)
			EndGame();

		else
			SpawnDart();
	}
}