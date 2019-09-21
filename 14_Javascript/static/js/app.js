// UFO Sighting JavaScript app

// D3 select
let tbody = d3.select("tbody");

// From data.js
var tableData = data;

// Creating function to build table
function buildTable(data) {
  // Clear data
  tbody.html("");
  // Loop through data in data.js file
  data.forEach((dataRow) => {
    // Append rows to tbody table
    let row = tbody.append("tr");
    // Iterate through values
    Object.values(dataRow).forEach((val) => {
      // Append row for each value
      let cell = row.append("td");
      cell.text(val);
    });

  })
}

// handleClick trigger when button is clicked
function handleClick() {
  // Prevents page from refreshing after each click
  d3.event.preventDefault();
  // Use d3 to select HTML datetime values
  let date = d3.select("#datetime").property("value");
  let filterData = tableData;

  // Apply filter to table
  if(date) {
    filterData = filterData.filter((row) => row.datetime === date);
  }
  // Build table
  buildTable(filterData);
}
// Filter on click event / trigger
d3.selectAll("#filter-btn").on("click", handleClick);
// Build table with the data in data.js file
buildTable(tableData);
