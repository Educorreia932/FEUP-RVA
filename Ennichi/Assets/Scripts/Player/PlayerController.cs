using System;
using TMPro;
using UnityEngine;

public class PlayerController : MonoBehaviour {
	public int points { get; set; }

	// Start is called before the first frame update
	void Start() {
		points = 300;
	}

	public void AddPoints(int amount) {
		points += amount;
	}
}