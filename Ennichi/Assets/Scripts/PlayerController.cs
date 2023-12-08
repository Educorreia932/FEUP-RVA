using System;
using TMPro;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
	private float speed = 5;
	private CharacterController controller;
	private PlayerTab playerTabScript;
	private UIManager uiManagerScript;

	public int points { get; set; }

	// Start is called before the first frame update
	void Start()
	{
		controller = GetComponent<CharacterController>();
		uiManagerScript = GameObject.FindGameObjectWithTag("MenuManager").GetComponent<UIManager>();
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

		// test points addition and menu updating
		if (Input.GetButtonDown("Jump"))
		{
			AddPoints(1);
		}

		if (Input.GetKeyDown(KeyCode.T))
		{
			uiManagerScript.ToggleUI();
		}
	}

	public void AddPoints(int amount)
	{
		points += amount;
		UpdatePointsText();
	}

	// Called only by the PlayerTab script, on its OnEnable Method
	public void SetPlayerTab(PlayerTab script)
	{
		playerTabScript = script;
	}

	// Called only by the PlayerTab script, on its OnDisable Method
	public void UnsetPlayerTab()
	{
		playerTabScript = null;
	}

	private void UpdatePointsText()
	{
		// menu is currently active, we want to hot reload it
		if (playerTabScript)
		{
			playerTabScript.UpdatePointsText(points);
		}
	}
}