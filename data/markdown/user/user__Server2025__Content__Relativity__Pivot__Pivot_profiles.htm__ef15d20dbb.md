---
title: "Pivot profiles"
url: https://help.relativity.com/Server2025/Content/Relativity/Pivot/Pivot_profiles.htm
collection: user
fetched_at: 2026-06-22T06:16:14+00:00
sha256: 8173ad652e6232ffed6f3ff0f7e8d5419a8868267554ceb9478d57ad72b53766
---

Pivot profiles Skip To Main Content Account Settings Logout

- placeholder

Account Settings Logout

relativitynd5u5rpx


https://help.relativity.com/Server2025/Content/CoveoSearch.htm


Coveo Search Page

>>

Version: RelativityOne Server 2025 Server 2024

☰

# Pivot profiles

Using Pivot profiles, you can create, save, and edit custom Pivot settings to use at any time. Once saved, these profiles are accessible via a drop-down menu in the upper-right corner of the item list.

Pivot profiles include configured settings for the Group By, Pivot On, and Date fields, as well as the chart formats. When you select a profile, the fields in the Pivot menu automatically populate with predefined values. You can modify these values to run additional Pivot reports. Use the Save button to save any updates to the preexisting profile or use the Save As button to create a new Pivot profile.

If you create a Pivot without selecting a profile, you can click Save to make the active settings into a profile. The Pivot profile does not save the documents associated with it.

You can't create or save modifications to Pivot Profiles unless you have the required permissions.

## Creating or editing a Pivot profile

Perform the following steps to create or edit a Pivot profile.

- Navigate to the Pivot Profiles tab, and then click New Pivot Profile . The Pivot Profile Information form appears with required fields in orange.

Only fields that have been Pivot-enabled will be available to select in this form.

- Complete the fields on the Pivot Profile Information form.

- Name - the name of the profile. You may want the name to reflect fields on which you pivoted.

- Object Type - the object type you would like this profile to appear under.

- Display - provides three check boxes to specify which of the three possible Pivot display types you want to be used to represent your profile in the item list:

- Pivot Grid - designates the grid as part of the profile display.

- Pivot Chart - designates the chart as part of the profile display.

- List - designates the list as part of the profile display.

- Group By - a list from which you select the field you want to act as your Group By value in your profile. Only fields that are Pivot-enabled on the Field page are available in this list.

Relativity does not recommend Group By for Long Text fields due to the performance impact. For more information, see Pivot .

- Group By Date - a drop-down menu providing the date values for the Group By field:

- Date - displays the date with day, month, and year.

- Week - displays week values.

- Two Weeks - displays every two weeks values.

- Year - displays only a year value.

- YearMonth - displays the year and month values.

- Pivot On - the Pivot On field in your profile. Only fields that are Pivot-enabled on the Field page are available in this list.

Relativity does not recommend Pivot On for Long Text fields due to the performance impact. For more information, see Pivot .

- Pivot On Date - provides the same dates for the Pivot On field as found above on Group By, with the addition of the following:

- Month - displays only a month value. Month is only available in Pivot On if your Group By field is also a date.

- Page Size - determines the number of sets per page in Pivot chart or graph. Depending on the display specifications you set, you may want to make this value low.

- Chart Type - determines what kind of chart is used to represent the profile in the item list:

- Bar - represents values in bar form.

- Pie - represents values in pie form.

- Line - represents values in line form.

- Chart Orientation - determines how the chart is positioned. There are two options:

- Horizontal - arranges values horizontally.

- Vertical - arranges values vertically.

- Sort On - determines the basis on which the chart information is sorted. There are two options:

- Grand Total - sorts by the total.

- Group By Field - sorts by the Group By field you specified.

- Descending - sorts starting with the first record and ending with the last.

- Sort Order - determines the order in which records are sorted. There are two options:

- Ascending - sorts starting with the last record and ending with the first.

- Switch Series - switches the Group By and Pivot On fields' positions.

- Toggles - configure additional chart instructions. The options are:

- Show Grand Total - toggles the display of grand total in the Pivot Chart. This value can help add context, but may throw off the scale of the Pivot Chart and reduce readability.

- Show Legend - toggles the display of the Pivot Chart legend. This information can often be intuited from looking at the chart. If not, it can be added.

- Show Blank Values - toggles the display of blank values in the chart.

- Rotate Labels - rotates the group by labels at a 45 degree angle. This can help readability in fields with many values.

- Stagger Labels - another option to improve readability of group by values. Stagger labels varies the horizontal position of the labels to improve readability.

- Show Labels - toggles the value count labels on Pivot Charts.

-

Show Sub-Chart – toggles the display of sub-chart in Bar Chart, Stacked Bar Chart, and Line Chart.

- Click Save .

On this page

- Pivot profiles

- Creating or editing a Pivot profile


Why was this not helpful?

Check one that applies.

I could not find the information I was looking for.

The information was incorrect.

The instructions are confusing or unclear.

The instructions did not work.

Thank you for your feedback.

Want to tell us more?


Great!

Thanks for taking the time to provide feedback.


- Install Relativity

- Pre-Installation

- Licensing

- Authentication

- Post-Installation verification test

- More >

- Upgrade

- Upgrade considerations

- Relativity upgrade

- More

- Infrastructure

- Servers

- Agents

- Resource pools

- Resource files

- More >

- Capabilities

- Analytics

- Processing

- More >

- Resources

- Relativity A-Z

- PDF Downloads

- Getting started

- Documentation archives

- Version support policy

- Relativity Learning

- Contact us

- 1-312-263-1177

- 231 South LaSalle Street 20th Floor Chicago, IL 60604

- © Relativity

- Privacy and Cookies

- Terms of Use
