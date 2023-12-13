using System;
using UnityEngine;

public class SkyboxController : MonoBehaviour {
	private enum DayTime {
		Morning,
		Afternoon,
		Evening,
		Night
	}

	public Material[] skyMaterials;

	void Update() {
		DayTime dayTime = DateTime.Now.Hour switch {
			< 12 => DayTime.Morning,
			< 18 => DayTime.Afternoon,
			< 21 => DayTime.Evening,
			_ => DayTime.Night
		};

		RenderSettings.skybox = skyMaterials[(int) dayTime];
	}
}