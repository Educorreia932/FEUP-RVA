using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DartsGameManager : MonoBehaviour
{
    public Transform spawnPoint;
    public GameObject dartPrefab;
    // Start is called before the first frame update
    void Start()
    {
        Instantiate(dartPrefab, spawnPoint);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
