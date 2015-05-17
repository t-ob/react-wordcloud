var WordCloud = React.createClass({
  render: function() {
    var words = this.props.data.map(function (word) {
      return (
        <div>
          {word.text} | {word.size}
        </div>
      );
    });
    return (
      <div className="wordCloud">
        {words}
      </div>
    );
  }
});

var WordCloudForm = React.createClass({
    handleSubmit: function(e) {
	e.preventDefault();
        var screen_name = React.findDOMNode(this.refs.screen_name).value.trim();
        if (!screen_name) {
          return;
        }
        this.props.onScreenNameSubmit({screen_name: screen_name});
        return;
    },
    render: function() {
      return (
        <form className="wordCloudForm" onSubmit={this.handleSubmit}>
          <input type="text" placeholder="Screen name" ref="screen_name" />
          <input type="submit" value="Post" />
        </form>
      );
    }
});


var WordCloudBox = React.createClass({
  handleScreenNameSubmit: function(screen_name) {
    $.ajax({
      url: this.props.url,
      datatype: 'json',
      type: 'POST',
      data: screen_name,
      success: function(data) {
        this.setState({data: data})
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []}
  },
  render: function() {
    return (
      <div className="wordCloudBox">
        <h1>Word Cloud</h1>
        <WordCloud data={this.state.data} />
        <WordCloudForm onScreenNameSubmit={this.handleScreenNameSubmit} />
      </div>
    );
  }
});

React.render(
  <WordCloudBox url="words.json" />,
  document.getElementById('content')
);
