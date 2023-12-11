using TMPro;
using UnityEngine;

public class CansGameManager : GameManager {
	public GameObject ballPrefab;
	public Transform ballSpawnPoint;
	public GameObject cansSpawnPoint;
	public GameObject canPyramidPrefab;
	public TextMeshProUGUI infoText;

	private int numBalls;
	private int cansFell;

	public override void StartGame() {
		numBalls = 5;
		cansFell = 0;

		UpdateText();

		SpawnBall();
		SpawnCans();

		canvas.SetActive(false);
	}

	protected override void EndGame() {
		canvas.SetActive(true);

		AwardPlayer(cansFell * 100);
	}

	public void SpawnBall() {
		Instantiate(ballPrefab, ballSpawnPoint);
	}

	public void SpawnCans() {
		// Delete existing cans
		DestroyCans();

		// Spawn pyramid of cans
		Instantiate(
			canPyramidPrefab,
			cansSpawnPoint.transform.position,
			cansSpawnPoint.transform.rotation,
			cansSpawnPoint.transform
		);
	}

	private void DestroyCans() {
		foreach (Transform child in cansSpawnPoint.transform)
			Destroy(child.gameObject);
	}

	public void BallFell() {
		numBalls--;
		UpdateText();

		if (numBalls == 0)
			EndGame();

		else
			SpawnBall();
	}

	public void CanFell() {
		cansFell++;
		UpdateText();

		// All cans fell
		if (cansFell == 6)
			EndGame();
		
	}

	public void UpdateText() {
		infoText.text = $"Cans fell: {cansFell}\nBalls left: {numBalls}";
	}
}