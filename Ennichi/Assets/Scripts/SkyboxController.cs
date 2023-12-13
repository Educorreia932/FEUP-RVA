using System;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class SkyboxController : MonoBehaviour {
	private enum DayTime {
		Morning,
		Afternoon,
		Evening,
		Night
	}

	public Material[] skyMaterials;
	public int overridenSkyMaterial;
	public TextMeshProUGUI skyboxText;

	void Update() {
		if (overridenSkyMaterial < 4) {
			RenderSettings.skybox = skyMaterials[overridenSkyMaterial];

			return;
		}

		DayTime dayTime = DateTime.Now.Hour switch {
			< 12 => DayTime.Morning,
			< 18 => DayTime.Afternoon,
			< 21 => DayTime.Evening,
			_ => DayTime.Night
		};

		RenderSettings.skybox = skyMaterials[(int) dayTime];
	}

	public void SetOverridenSkyMaterial(Slider slider) {
		overridenSkyMaterial = (int) slider.value;

		skyboxText.text = overridenSkyMaterial switch {
			0 => "Morning",
			1 => "Afternoon",
			2 => "Evening",
			3 => "Night",
			_ => "Dynamic"
		};
	}
}