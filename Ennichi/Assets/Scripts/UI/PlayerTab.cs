using System.Collections;
using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class PlayerTab : Tab
{
    PlayerController playerScript;
    TMP_Text pointsText;

    void Start()
    {
        Debug.Log("hi");
    }

    protected override void OnEnable()
    {
        playerScript = GameObject.FindGameObjectWithTag("Player").GetComponent<PlayerController>();
        playerScript.SetPlayerTab(this);
        pointsText = GameObject.FindGameObjectWithTag("PlayerPointsText").GetComponent<TMP_Text>();
        UpdatePointsText(playerScript.points);
    }

    protected override void OnDisable()
    {
        playerScript.UnsetPlayerTab();
    }

    public void UpdatePointsText(int points)
    {
        pointsText.text = "Points: " + points;
    }
}
