using TMPro;
using UnityEngine;

public class PlayerController : MonoBehaviour {
	public TextMeshProUGUI pointsText;
	
	public int points { get; set; }

	void Start() {
		points = 0;
	}

	public void AddPoints(int amount) {
		points += amount;
		
		pointsText.text = $"Coins: {points}";
	}
	
	public void RemovePoints(int amount) {
		points -= amount;
		
		pointsText.text = $"Coins: {points}";
	}
}