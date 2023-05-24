backports.zoneinfo==0.2.1
#africastalking==1.2.5
#aiohttp==3.8.4
    <h1>Reservation List</h1>
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>Reservation ID</th>
                <th>Guest name</th>
                <th>Guest number</th>
                <th>Checked-in</th>
                <th>Payment</th>
                <th>Nights</th>
                <th>ARRIVES</th>
                <th>DEPARTS</th>
                <th>Room</th>
                <th>GROUP</th>
                <th>Room Status</th>
                
            </tr>
        </thead>
        <tbody>
            {% for reservation in reservations %}
                <tr>
                    <td><a href="{% url 'reservation_detail' reservation.id %}">{{ reservation.id }}</a></td>
                    <td>{{ reservation.guest }}</td>
                    <td>{{ reservation.num_of_guests }}</td>
                    <td>....</td>
                    <td>{{ reservation.total_charge }}</td>
                    <td>{{ reservation.num_of_nights }}</td>
                    <td>{{ reservation.check_in_date }}</td>
                    <td>{{ reservation.check_out_date }}</td>
                    <td>{{ reservation.room }}</td>
                    <td>.....</td>
                    <td>.....</td>
                    
                </tr>
            {% empty %}
                <tr>
                    <td colspan="7">No reservations found.</td>
                </tr>
            {% endfor %}
        </tbody>
    </table> 
    <style>
      .tick {
          color: green;
      }
  </style>
    <h2>Arriving Reservations</h2>
    <table class="table table-bordered">
        <thead>
            <tr>
              <th>Checked In</th>
                <th>Reservation ID</th>
                <th>Guest</th>
                <th>CHECKED IN</th>
                <th>Room</th>
                <th>Check-in Date</th>
                <th>Check-out Date</th>
                <th>Number of Nights</th>
                <th>Payment Status</th>
                <th>Total Charge</th>
            </tr>
        </thead>
        <tbody>
            {% for reservation in reservations %}
                {% if reservation.event_type == "Arriving" %}
                    <tr>
                      <td>
                        <input type="checkbox" id="arrival_{{ reservation.id }}" name="arrival_checkbox" {% if reservation.checking == 'Checked In' %}checked{% endif %}>
                    </td>
                        <td><a href="{% url 'reservation_detail' reservation.id %}">{{ reservation.id }}</a></td>
                        <td>{{ reservation.guest }}</td>
                        <td>
                          {% if reservation.checking == 'Checked In' %}
                              <span class="tick">&#10004;</span>
                          {% else %}
                              ~
                          {% endif %}
                      </td>
                        <td>{{ reservation.room }}</td>
                        <td>{{ reservation.check_in_date }}</td>
                        <td>{{ reservation.check_out_date }}</td>
                        <td>{{ reservation.num_of_nights }}</td>
                        <td>{{ reservation.payment_status }}</td>
                        <td>{{ reservation.total_charge }}</td>
                    </tr>

                    <script>
                      document.getElementById('arrival_{{ reservation.id }}').addEventListener('change', function() {
                          var checkbox = this;
                          var reservationId = checkbox.id.split('_')[1];

                          if (checkbox.checked) {
                              fetch('/front_desk/reservations/' + reservationId + '/checkin/', {
                                  method: 'POST',
                                  headers: {
                                      'X-CSRFToken': '{{ csrf_token }}',
                                      'Content-Type': 'application/json'
                                  },
                                  body: JSON.stringify({ checking: 'Checked In' })
                              })
                              .then(function(response) {
                                  if (!response.ok) {
                                      throw new Error('Error updating check-in status');
                                  }
                              })
                              .catch(function(error) {
                                  console.log(error);
                              });
                          }
                      });
                  </script>
                {% endif %}
            {% empty %}
                <tr>
                    <td colspan="8">No arriving reservations found.</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
    <h2>Departing Reservations</h2>
    <table class="table table-bordered">
        <thead>
            <tr>
              <th>Checked Out</th>
                <th>Reservation ID</th>
                <th>CHECKED OUT</th>
                <th>Guest</th>
                <th>Room</th>
                <th>Check-in Date</th>
                <th>Check-out Date</th>
                <th>Number of Nights</th>
                <th>Payment Status</th>
                <th>Total Charge</th>
            </tr>
        </thead>
        <tbody>
            {% for reservation in reservations %}
                {% if reservation.event_type == "Departing" %}
                    <tr>
                      <td>
                        <input type="checkbox" id="departure_{{ reservation.id }}" name="departure_checkbox" {% if reservation.checking == 'Checked Out' %}checked{% endif %}>
                    </td>
                        <td><a href="{% url 'reservation_detail' reservation.id %}">{{ reservation.id }}</a></td>
                        <td>
                          {% if reservation.checking == 'Checked Out' %}
                              <span class="tick">&#10004;</span>
                          {% else %}
                              No
                          {% endif %}
                      </td>
                        <td>{{ reservation.guest }}</td>
                        <td>{{ reservation.room }}</td>
                        <td>{{ reservation.check_in_date }}</td>
                        <td>{{ reservation.check_out_date }}</td>
                        <td>{{ reservation.num_of_nights }}</td>
                        <td>{{ reservation.payment_status }}</td>
                        <td>{{ reservation.total_charge }}</td>
                    </tr>
                    <script>
                      document.getElementById('departure_{{ reservation.id }}').addEventListener('change', function() {
                          var checkbox = this;
                          var reservationId = checkbox.id.split('_')[1];

                          if (checkbox.checked) {
                              fetch('/front_desk/reservations/' + reservationId + '/checkout/', {
                                  method: 'POST',
                                  headers: {
                                      'X-CSRFToken': '{{ csrf_token }}',
                                      'Content-Type': 'application/json'
                                  },
                                  body: JSON.stringify({ checking: 'Checked Out' })
                              })
                              .then(function(response) {
                                  if (!response.ok) {
                                      throw new Error('Error updating check-out status');
                                  }
                              })
                              .catch(function(error) {
                                  console.log(error);
                              });
                          }
                      });
                  </script>
                {% endif %}
            {% empty %}
                <tr>
                    <td colspan="8">No departing reservations found.</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>

    <h2>Staying Over Reservations</h2>
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>Reservation ID</th>
                <th>Guest</th>
                <th>Day</th>
                <th>Room</th>
                <th>Check-in Date</th>
                <th>Check-out Date</th>
                <th>Number of Nights</th>
                <th>Number of Days Stayed</th>
                <th>Payment Status</th>
                <th>Total Charge</th>
            </tr>
        </thead>
        <tbody>
            {% for reservation in reservations %}
                {% if reservation.event_type == "Staying Over" %}
                    <tr>
                        <td><a href="{% url 'reservation_detail' reservation.id %}">{{ reservation.id }}</a></td>
                        <td>{{ reservation.guest }}</td>
                        <td>{{ reservation.num_of_nights_spent }}</td>
                        <td>{{ reservation.room }}</td>
                        <td>{{ reservation.check_in_date }}</td>
                        <td>{{ reservation.check_out_date }}</td>
                        <td>{{ reservation.num_of_nights }}</td>
                        <td>{{ reservation.num_of_days_stayed }}</td>
                        <td>{{ reservation.payment_status }}</td>
                        <td>{{ reservation.total_charge }}</td>
                    </tr>
                {% endif %}
            {% empty %}
                <tr>
                    <td colspan="9">No staying over reservations found.</td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
