
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
    d3.tsv("data/titanic.csv", function (data) {
              var chart = new dimple.chart(svg, data);
              chart.addCategoryAxis("x", ["Class","Survival"]);
              chart.addMeasureAxis("y", "Count");
              chart.addSeries("Survival", dimple.plot.bar);
              chart.addLegend(65, 10, 510, 20, "right");
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
 


