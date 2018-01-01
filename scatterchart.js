var margin = {top: 20, right: 60, bottom: 60, left: 60}
  , width = 960 - margin.left - margin.right
  , height = 500 - margin.top - margin.bottom;

var x = d3.scale.linear()
          .domain([
            d3.min(data, function(d) { return d[1]; }),
            d3.max(data, function(d) { return d[1]; })
          ])
          .range([ 0, width ]);

var y = d3.scale.linear()
        .domain([0, d3.max(data, function(d) { return d[2]; })])
        .range([ height, 0 ]);

var chart = d3.select('body')
.append('svg:svg')
.attr('width', width + margin.right + margin.left)
.attr('height', height + margin.top + margin.bottom)
.attr('class', 'chart')

var main = chart.append('g')
.attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')
.attr('width', width)
.attr('height', height)
.attr('class', 'main')

// draw the x axis
var xAxis = d3.svg.axis()
.scale(x)
.orient('bottom');

main.append('g')
.attr('transform', 'translate(0,' + height + ')')
.attr('class', 'main axis date')
.call(xAxis);

// draw the y axis
var yAxis = d3.svg.axis()
.scale(y)
.orient('left');

main.append('g')
.attr('transform', 'translate(0,0)')
.attr('class', 'main axis date')
.call(yAxis);

var g = main.append("svg:g");

g.selectAll("scatter-dots")
  .data(data)
  .enter().append("svg:circle")
      .attr("cx", function (d,i) { return x(d[1]); } )
      .attr("cy", function (d) { return y(d[2]); } )
      .attr("r", 4);


g.selectAll("text")
  .data(data)
  .enter().append("text")
    .text(function(d) {
        return d[0];
    })
    .attr("x", function(d) {
        return x(d[1]) + 5;  // Returns scaled location of x
    })
    .attr("y", function(d) {
        return y(d[2]);  // Returns scaled circle y
    })
    .attr("font_family", "sans-serif")  // Font type
    .attr("font-size", "14px")  // Font size
