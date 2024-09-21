#!/bin/bash

# Navigate to the project root directory
cd "$(dirname "$0")"

# Start the Streamlit frontend on port 8001
echo "Starting the Streamlit frontend..."
nohup streamlit run main.py --server.port 8002 > frontend.log 2>&1 &
FRONTEND_PID=$!
echo "Streamlit frontend started with PID $FRONTEND_PID"

# Save the PID to a file for easy shutdown later
echo $FRONTEND_PID > pid.txt

echo "The Streamlit process is now running in the background."
echo "You can view the frontend logs in frontend.log"
echo "To stop the process, run: ./stopgard.sh"

# Display the Streamlit access link
echo "Access the Streamlit frontend at: http://localhost:8002"

# Create a stop script
cat << EOF > stopgard.sh
#!/bin/bash
if [ -f pid.txt ]; then
  pid=\$(cat pid.txt)
  if ps -p \$pid > /dev/null; then
    echo "Stopping process \$pid"
    kill \$pid
  fi
  rm pid.txt
  echo "Process stopped"
else
  echo "No pid.txt file found. Process may not be running."
fi
EOF

chmod +x stop.sh
echo "A stop script has been created. Run ./stopgard.sh to stop the process."
