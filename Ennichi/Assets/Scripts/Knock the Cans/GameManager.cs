using UnityEngine;

public class GameManager : MonoBehaviour {
	public GameObject ballPrefab;
	public Transform ballSpawnPoint;
	public GameObject canvas;
	public GameObject cans;
	public GameObject canPyramidPrefab;

	private int numBalls;
	private int cansFell;

	public void StartGame() {
		numBalls = 5;
		cansFell = 0;

		SpawnBall();
		SpawnCans();

		canvas.SetActive(false);
	}

	private void EndGame() {
		canvas.SetActive(true);

		// Reward points
	}

	public void SpawnBall() {
		Instantiate(ballPrefab, ballSpawnPoint);
	}

	public void SpawnCans() {
		// Delete existing cans
		DestroyCans();

		// Spawn pyramid of cans
		Instantiate(canPyramidPrefab, cans.transform.position, cans.transform.rotation, cans.transform);
	}

	private void DestroyCans() {
		foreach (Transform child in cans.transform)
			Destroy(child.gameObject);
	}

	public void BallFell() {
		numBalls--;

		if (numBalls == 0) {
			EndGame();
		}

		else {
			SpawnBall();
		}
	}

	public void CanFell() {
		cansFell++;
		
		// All cans fell
		if (cansFell == 6)
			EndGame();
	}
}