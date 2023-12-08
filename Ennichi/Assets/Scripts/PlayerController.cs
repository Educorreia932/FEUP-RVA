using System;
using TMPro;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
	private float speed = 5;
	private CharacterController controller;
	private int points;
	private TMP_Text pointsText;

	// Start is called before the first frame update
	void Start()
	{
		controller = GetComponent<CharacterController>();
		pointsText = GameObject.FindGameObjectWithTag("UIPoints").GetComponent<TMP_Text>();
		points = 0;
		UpdatePointsText();
	}

	// Update is called once per frame
	void Update()
	{
		// Get input
		Vector3 input = new(
			Input.GetAxisRaw("Horizontal"),
			0,
			Input.GetAxisRaw("Vertical")
		);

		input = input.normalized;

		Vector3 velocity = input * speed;

		// Move player
		controller.Move(velocity * Time.deltaTime);
	}

	public void AddPoints(int amount)
	{
		points += amount;
		UpdatePointsText();
	}

	private void UpdatePointsText()
	{
		pointsText.text = "Points: " + points;
	}
}