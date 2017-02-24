
// header
    var Title = d3.select('#title')
                                .append("h2")
                                .attr("width",590)
                                .attr("height",400)
                                .text("Survival Chance on the Titanic's passange");
//description 
    var Header = d3.select('#description')
                                .append("h3")
                                .text("CRMS titanic was a British passenger liner that sank in the North Atlantic Ocean in the early morning of 15 April 1912, after colliding with an iceberg during her maiden voyage from Southampton to New York City. Of the 2,224 passengers and crew aboard, more than 1,500 died in the sinking.")
                                .attr("align","center");
       



//Chart 1
    var svg = dimple.newSvg("#chart1", 590, 400);
    d3.csv("data/titanic.csv", function (data) {
              var chart = new dimple.chart(svg, data);
              var xAxis = chart.addCategoryAxis("x", ["Class","Sex"]);
              xAxis.addOrderRule(["First", "Second", "Third"]);
              var yAxis = chart.addMeasureAxis("y", "Count");
              var Series = chart.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              /*chart.addOrderRule(["Survived","Perished"]);*/
              var Legend = chart.addLegend(65, 10, 510, 20, "right");
              chart.assignColor("female", "rgb(128, 177, 211)", "rgb(107, 148, 176)", 0.8);
              chart.assignColor("male","rgb(251, 128, 114)","rgb(210, 107, 95)", 0.8);
              svg.append("text")
              // Position in the center of the shape (vertical position is
              // manually set due to cross-browser problems with baseline)
                .attr("x", chart._xPixels() + chart._widthPixels() / 2)
                .attr("y", chart._yPixels() - 20)
                 // Align to center
                .style("text-anchor", "middle")
                .style("font-weight", "bold")
                .style("font-family", "sans-serif")
                .text("Survival Rate per class ")
    chart.draw();
    
    });
 

//description graph1
    var Desc1 = d3.select('#chart1desc')
                                .append("h4")
                                .text("We can observed that majority of passangers in third class persihed. ")
                                .attr("align","center");



//Chart 2
    var svg2 = dimple.newSvg("#chart2", 590, 400);
    d3.csv("data/titanic.csv", function (data) {
              var chart2 = new dimple.chart(svg2, data);
              var xAxis = chart2.addCategoryAxis("x", ["Embarked","Sex"]);
              var yAxis = chart2.addPctAxis("y", "Count");
              var Series = chart2.addSeries("Survived", dimple.plot.bar);
              Series.addOrderRule(["Survived","Perished"]);
              /*chart.addOrderRule(["Survived","Perished"]);*/
              var Legend = chart2.addLegend(65, 10, 510, 20, "right");
              chart2.assignColor("female", "rgb(128, 177, 211)", "rgb(107, 148, 176)", 0.8);
              chart2.assignColor("male","rgb(251, 128, 114)","rgb(210, 107, 95)", 0.8);
              svg2.append("text")
              // Position in the center of the shape (vertical position is
              // manually set due to cross-browser problems with baseline)
                .attr("x", chart2._xPixels() + chart2._widthPixels() / 2)
                .attr("y", chart2._yPixels() - 20)
                 // Align to center
                .style("text-anchor", "middle")
                .style("font-weight", "bold")
                .style("font-family", "sans-serif")
                .text("Survival Rate per class ")
    chart2.draw();
    
    });

//description graph1
    var Desc2 = d3.select('#chart2desc')
                                .append("h4")
                                .text("bla bla bla")
                                .attr("align","center")