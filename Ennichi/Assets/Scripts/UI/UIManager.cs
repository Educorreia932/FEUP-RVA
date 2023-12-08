using System.Collections;
using System.Collections.Generic;
using Unity.XR.CoreUtils;
using UnityEngine;

public class UIManager : MonoBehaviour
{
    public TabSystem tabSystem;
    private List<GameObject> tabs;
    private int currentTabIndex;

    void Start()
    {
        tabSystem = GameObject.FindGameObjectWithTag("MenuButtons").GetComponent<TabSystem>();
        tabSystem.TabButtonAmount = 4;
        currentTabIndex = -1;
        tabSystem.SetSelectedButtonIndex(0);
        tabSystem.OnTabButtonsClicked.AddListener(EventExample);
        tabs = GetTabs();
        DisableTabs();
    }

    private List<GameObject> GetTabs()
    {
        List<GameObject> tabs = new List<GameObject>();
        foreach (Transform child in GameObject.FindGameObjectWithTag("MenuTabs").transform)
        {
            tabs.Add(child.gameObject);
        }
        return tabs;
    }

    private void ToggleMenu()
    {
        gameObject.SetActive(!gameObject.activeSelf);
    }

    private void DisableTab(int tabIndex)
    {
        GameObject tabObj = tabs[tabIndex];
        if (tabObj == null)
        {
            Debug.LogError("Tab " + tabIndex + " is undefined.");
            return;
        }
        tabObj.SetActive(false);
    }

    private void EnableTab(int tabIndex)
    {
        GameObject tabObj = tabs[tabIndex];
        if (tabObj == null)
        {
            Debug.LogError("Tab " + tabIndex + " is undefined.");
            return;
        }
        tabObj.SetActive(true);
    }

    private void DisableTabs()
    {
        foreach (GameObject tab in tabs)
        {
            tab.SetActive(false);
        }
    }

    private void EnableTabs()
    {
        foreach (GameObject tab in tabs)
        {
            tab.SetActive(true);
        }
    }

    private void ToggleTab(int tabIndex)
    {
        GameObject tabObj = tabs[tabIndex];
        if (tabObj == null)
        {
            Debug.LogError("Tab " + tabIndex + " is undefined.");
            return;
        }
        tabObj.SetActive(!tabObj.activeSelf);
    }

    // ...
    // Register this event from inspector if you want, using the unity event.
    public void EventExample(int selectedTabIndex)
    {
        // untoggle current tab
        if (selectedTabIndex == currentTabIndex)
        {
            ToggleTab(currentTabIndex);
            currentTabIndex = -1;
            return;
        }

        // check if another tab is currently active
        if (currentTabIndex != -1)
        {
            // toggle it off
            ToggleTab(currentTabIndex);
        }

        // toggle on new tab
        ToggleTab(selectedTabIndex);
        currentTabIndex = selectedTabIndex;
    }
}
