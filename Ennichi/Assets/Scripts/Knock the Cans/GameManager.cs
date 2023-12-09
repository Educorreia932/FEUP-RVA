using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameManager : MonoBehaviour {
	public GameObject ballPrefab;
	public Transform ballSpawnPoint;
	public GameObject canvas;

	public void StartGame() {
		SpawnBall();
		
		canvas.SetActive(false);
	}

	public void SpawnBall() {
		Instantiate(ballPrefab, ballSpawnPoint);
	}

	public void SpawnCans() {
	}

	void Update() {
	}
}